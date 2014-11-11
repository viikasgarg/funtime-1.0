var timer;
var puzzleValues = [];
// level = size-2
// score = (size -3)*(size-3)*50
var level = 1;
var attempt = 0;
var primary_btns = [];
var selected_values = [];

function updateScore(){
    $('#level').html(level);
    $('#score').html((level-1)*(level-1)*50);
    primary_btns.length = 0;
    selected_values.length = 0;
    puzzleValues.length = 0;
    attempt = 0;
    }

function startGame(){
    if (level>1) level--;
    $("#help").hide();
    $("#game").show();
    updateScore();
    $("#game-object").guesscolor(level+3, level+5, 10-level);
}

function nextLevel() {
    level++;
    updateScore();
    $("#game-object").guesscolor(level+3, level+5, 10-level);
}




function simpleStopWatch(value,dialog){
    $("#timer").html(value);
    if(value-- <= 0){
        if(dialog) {
            clearTimeout(timer);
            $("#dialog-timeup" ).dialog( "open" );
        }
        return 0;
    }else {
        timer = setTimeout('simpleStopWatch('+value+"," + dialog+')',1000);
    }
    return 1;
}

function get_option_table(range){

    var option_btn = '<img id="img_%id" class="trans_image" onclick="checkValue(%id);" src="/static/guesscolor/images/%id.jpg" />';
    var option_table = $('<table class="option_row"/>');

    var tr = $('<tr/>');
    for(j=1; j<range+1; j++) {
        var td = $('<td/>');
        btn = option_btn.replace("%id", j).replace("%id", j).replace("%id", j);
        td.append(btn);
        tr.append(td);
    }
    option_table.append(tr);
    return option_table;
}

function get_primary_table(size, tries){
    var primary_btn = '<img id="primary_%id" class="trans_image" src="/static/guesscolor/images/blank.png" />';
    var table = $('<table class="tofill_grid"/>');
    primary_btns.length = 0;
    for(i=0; i<tries; i++) {
        var tr = $('<tr/>');
        for(j=1; j<=size; j++) {
            var td = $('<td/>');
            btn = primary_btn.replace("%id", i*size+j);
            primary_btns.push(btn);
            td.append(btn);
            tr.append(td);
        }
        table.append(tr);
    }
    return table;
}


function get_attempt_table(size, tries){
    var table = $('<table class="attempt_grid"/>');
    for(i=0; i<tries; i++) {
        var tr = $('<tr/>');
        for(j=1; j<=size; j++) {
            var td = ('<td id="attempt_%id"/>');
            btn = td.replace("%id", i*size +j);
            tr.append($(btn));
        }
        table.append(tr);
    }
    return table;
}

function grid(context, size, range, tries) {
    var div = $(context);
    div.empty();

    var main_table = $('<table class="game_table"/>').attr("width","100%");
    var first_tr = $('<tr/>');

    // create board where we will fill data
    var option_td = $('<td/>').attr("colspan", 2);
    option_td.append(get_option_table(range));
    first_tr.append(option_td);
    main_table.append(first_tr);

    var second_tr = $('<tr/>');
    var primary_td = $('<td/>');
    primary_td.append(get_primary_table(size, tries));
    second_tr.append(primary_td);

    var attempt_td = $('<td/>');
    attempt_td.append(get_attempt_table(size, tries));
    second_tr.append(attempt_td);

    main_table.append(second_tr);
    div.append(main_table);
}


function createValues(size, range){
    var temp_values = [];
    var ret_values = [];
    for (i=0; i<range; i++) {
        temp_values.push(i+1);
    }
    for(i=0; i< size; i++) {
        value = Math.floor(Math.random()*10%range);
        ret_values.push(temp_values[value]);
        temp_values.splice(value,1);
        range--;
    }
    return ret_values;
}

function get_exact_match(){
    count = 0;
    for(i=0; i<puzzleValues.length; i++){
        if(selected_values[i] == puzzleValues[i]){
            count++;
        }
    }
    return count;
}


function get_approx_match(){
    count =0;
    for(i=0; i<puzzleValues.length; i++){
        index = selected_values.indexOf(puzzleValues[i]);
        if( index != -1 && index != i){
            count++;
        }
    }
    return count;
}

function update_attempt_table(exact_match, approx_match){
    var exact_btn = '<img class="trans_image" src="/static/guesscolor/images/same.jpg" />';
    var approx_btn = '<img class="trans_image" src="/static/guesscolor/images/approx.jpg" />';
    var question_btn = '<img class="trans_image" src="/static/guesscolor/images/question.jpg" />';

    var i = attempt - puzzleValues.length;
    for(j=1; j<=exact_match; j++){
        if((i+j)<=attempt) {
            $("#attempt_"+(i+j)).append(exact_btn);
        }
    }
    i = i + j-1;

    for(j=1; j<=approx_match; j++){
        if((i+j)<=attempt) {
            $("#attempt_"+(i+j)).append(approx_btn);
        }
    }
    i = i + j-1;
    for(j=1;j<=attempt; j++){
        if((i+j)<=attempt) {
            $("#attempt_"+(i+j)).append(question_btn);
        }
    }
}

function checkValue(id){
    var button_pressed = '#img_' +id;
    attempt ++;
    if(attempt < primary_btns.length){
        $("#primary_"+attempt).attr("src",$(button_pressed).attr('src'));
        selected_values.push(id);
        if (attempt%puzzleValues.length === 0) {
            exact_match = get_exact_match();
            if(exact_match == puzzleValues.length){
                clearTimeout(timer);
                $( "#dialog-congrats" ).dialog( "open" );
            }
            approx_match = get_approx_match();
            update_attempt_table(exact_match, approx_match);
            selected_values.length = 0;
        }
    }
    else {
        clearTimeout(timer);
        $( "#dialog-triesdone" ).dialog( "open" );
    }
}


function createPuzzle(context, size, range, tries) {
        values = createValues(size, range);
        grid(context, size, range, tries);
        return values;
    }

$.fn.extend({
    guesscolor: function(size, range, tries){
                    puzzleValues = createPuzzle(this, size, range, tries);
                    var context = this;
                    var side = size;
                    var range_values = range;
                    var tries_values = tries;
                    simpleStopWatch((size-2)*100, true);
                    /*
                    setTimeout(function createPlayingBoard() {
                                        clearTimeout(timer);
                                        values = createValues(side, side+2);
                                        grid(context, side, range_values, tries_values);
                                        timer =  // for open dialog
                                    } ,1000);*/
        }
});


