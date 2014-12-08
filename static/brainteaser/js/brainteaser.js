var timer;
var count = 0;
var foundCount = 0;
var puzzleValues;
var level = 1;

function updateScore(){
    count = 0;
    foundCount = 0;
    $('#level').html(level);
    $('#score').html((level-1)*(level-1)*50);
    }

function startGame(){
    if (level>1) level--;
    $("#help").hide();
    $("#game").show();
    updateScore();
    $("#game-object").brainteaser(level+2);
}

function nextLevel() {
    level++;
    updateScore();
    $("#game-object").brainteaser(level+2);
}


function simpleStopWatch(value, dialog){
    $("#timer").html(value);
    if(value-- <= 0){
        if(dialog) {
            clearTimeout(timer);
            $("#dialog-timeup" ).dialog( "open" );
        }
        return 0;
    }else {
        timer = setTimeout('simpleStopWatch('+value+"," + dialog+')', 1000);
    }
    return 1;
}


function grid(context,size,values,noclick) {
    var div = $(context);
    div.empty();
    var primary_btn = '<a  type="button" class="btn btn-primary box" />';
    var success_btn = '<a  id=%id onclick="checkValue(%s);" type="button" class="btn btn-success box" />';
    if(noclick) {
        success_btn = '<a  id=%id type="button" class="btn btn-success box" />';
    }
    var danger_btn =  '<a  type="button" class="btn btn-danger box" />';
    var table = $('<table/>').attr("border",1).attr("width","100%").attr("height","100%");
    for(i=0; i<size; i++) {
        var tr = $('<tr/>');
        for(j=0; j<size; j++) {
            var td = $('<td/>');
            if (values[i*size+j] === 0) {
                var id = "btn_" + (i*size+j);
                if(noclick) {
                    button = success_btn.replace("%id",id);
                }
                else {
                    button = success_btn.replace("%s",(i*size+j)).replace("%id",id);
                }
            }
            else {
                button = danger_btn;
            }
            td.append(button);
            tr.append(td);
        }
        table.append(tr);
    }
    div.append(table);
}


function createValues(size,range){
    values = [];
    for(i=0; i<size; i++) {
        value = Math.floor(Math.random()*10%range);
        if(value == 1) count++;
        values.push(value);
    }

    return values;
}


function checkValue(id){
    var button_pressed = '#btn_' +id;
    $(button_pressed).removeClass("btn-success");
    if(puzzleValues[id] == 1) {
        $(button_pressed).addClass("btn-danger");
        foundCount++;
        if(foundCount == count) {
            clearTimeout(timer);
            $( "#dialog-congrats" ).dialog( "open" );
        }
    }else {
        clearTimeout(timer);
        $( "#dialog-wrongpressed" ).dialog( "open" );
        $(button_pressed).addClass("btn-primary");
    }
}


function createPuzzle(context,size) {
        clearTimeout(timer);
        values = createValues(size*size,2);
        grid(context,size,values,true);
        timer = simpleStopWatch(size*2,false); // false for open dialog
        return values;
    }

$.fn.extend({
    brainteaser: function(size){
                    puzzleValues = createPuzzle(this, size);
                    var context = this;
                    var side = size;
                    setTimeout(function createPlayingBoard() {
                                        clearTimeout(timer);
                                        values = createValues(side*side, 1);
                                        grid(context, side, values, false);
                                        timer = simpleStopWatch(side*2, true); // for open dialog
                                    } ,
                                size*2000);

        }
});


