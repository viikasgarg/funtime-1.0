import datetime
from django.template import RequestContext,loader,Context
from sudokusolver.forms import GridForm
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from sudokusolver.sudsolver import Sudoku as SudokuSolver
from  sudokusolver.models import Sudoku
import json
import random

def home(request):
    grid_form = GridForm(request.POST or None, grid_name="sudoku",rows=9,cols=9)
    if "POST" == request.method:
        ## Solve Sudoku
        if grid_form.is_valid():

            puzzle_data =  grid_form.cleaned_data
            sudoku =  SudokuSolver(puzzle_data)
            sudoku.solve()
            if sudoku.complete:
                sudoku_object = Sudoku()
                sudoku_object.puzzle_data = json.dumps(puzzle_data)
                sudoku_object.solution_data = json.dumps(sudoku.data)
                sudoku_object.timetaken = str(sudoku.duration*1000)

                if 0 < sudoku.duration*1000 < 1000:
                    level = "easy"
                elif 1000 < sudoku.duration*1000 < 2000:
                    level = "medium"
                else:
                    level = "hard"
                sudoku_object.level = level
                sudoku_object.save()

            sol_form = GridForm(grid_name="sol",rows=9,cols=9,readonly=True,initial_data=sudoku.data)
            return render_to_response('brainteaser.html', {'grid_form':grid_form,
                                    'sol_form':sol_form
                                },
                                context_instance = RequestContext(request))

    return render_to_response('brainteaser.html', {'grid_form':grid_form},
                                context_instance = RequestContext(request))

