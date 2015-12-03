import copy
from time import time


class Sudoku:

    def __init__(self, data):
        self.data = copy.deepcopy(data)
        self.oldrow = copy.deepcopy(data)

    def solve(self):
        start = time()
        self.values = []
        for i in range(0, 9):
            lst = []
            for j in range(0, 9):
                if not self.data[i][j]:
                    k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    lst.append(k)

                else:
                    lst.append([int(self.data[i][j])])
            self.values.append(lst)
        self.crack()
        self.letattack()
        self.complete = (self.check() == 2)
        self.duration = time() - start

    def crack(self):
        work = 0
        for i in range(0, 9):
            for j in range(0, 9):
                k = self.data[i][j]

                if k:
                    for l in range(0, 9):
                        if len(self.values[i][l]) != 1 and int(
                                k) in self.values[i][l]:
                            self.values[i][l].remove(int(k))
                            if len(self.values[i][l]) == 1:
                                self.data[i][l] = self.values[i][l][0]
                                work = 1
                            # print i,l,self.values[i][l],k +"\n"
                    for l in range(0, 9):
                        if len(self.values[l][j]) != 1 and int(
                                k) in self.values[l][j]:
                            self.values[l][j].remove(int(k))
                            if len(self.values[l][j]) == 1:
                                self.data[l][j] = self.values[l][j][0]
                                work = 1
                            # print l,j,self.values[l][j],k +"\n"

                    for l in range(0, 9):
                        if len(self.values[i - (i %3) + l / 3][j - (j % 3) + l %
                                                            3]) != 1 and int(k) in self.values[
                                                             i - (i % 3) + l / 3][j - (j % 3) + l % 3]:
                            self.values[i - (i % 3) + l / 3][j - (j % 3) + l % 3].remove(int(k))
                            if len(self.values[i - (i % 3) + l / 3][j - (j % 3) + l % 3]) == 1:
                                self.data[i - (i % 3) + l / 3][j - (j % 3) + l % 3] = self.values[
                                                                i - (i %3) + l / 3][j - (j % 3) + l % 3][0]
                                work = 1


        if work:
            self.crack()

        return

    def letattack(self):
        sort = []

        for i in range(0, 8):
            s1 = []
            sort.append(s1)
        for i in range(0, 9):
            for j in range(0, 9):
                if len(self.values[i][j]) > 1:
                    sort[len(self.values[i][j]) -
                         2].append([self.values[i][j], i, j])
        # print sort[1]
        noerror = 1
        for k in range(0, 7):
            for value in sort[k]:
                remov = 0
                for time in range(0, len(value[0])):
                    if int(
                            value[0][
                                time -
                                remov]) in self.values[
                            value[1]][
                            value[2]]:
                        self.oldvalues = copy.deepcopy(self.values)
                        self.copysud(self.oldrow, self.data)
                        self.values[
                            value[1]][
                            value[2]] = [
                            value[0][
                                time -
                                remov]]
                        self.data[value[1]][value[2]] = value[0][time - remov]
                        self.crack()
                        error = self.check()
                        if error == 2:
                            return
                        self.copysud(self.data, self.oldrow)
                        self.values = copy.deepcopy(self.oldvalues)

                        if error:
                            noerror = 0
                            # print "\nerror  "
                            # print
                            # self.values[value[1]][value[2]],value[1],value[2]
                            if int(
                                    value[0][
                                        time -
                                        remov]) in self.values[
                                    value[1]][
                                    value[2]]:
                                self.values[value[1]][value[2]].remove(
                                    int(value[0][time - remov]))
                            remov = remov + 1
                            if(len(self.values[value[1]][value[2]]) == 1):
                                self.data[
                                    value[1]][
                                    value[2]] = self.values[
                                    value[1]][
                                    value[2]][0]
                        self.crack()
        if noerror:
            return
        else:
            self.letattack()

    def copysud(self, list1, list2):
        for i in range(0, 9):
            for j in range(0, 9):
                list1[i][j] = list2[i][j]

    def check(self):
        " this function return 1 (a error signal if a row or column will contain more than 2 characters)"
        s = 0
        comp = 1
        for i in range(0, 9):
            testlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0, 9):
                if self.data[i][j]:
                    if int(self.data[i][j]) in testlist:
                        testlist.remove(int(self.data[i][j]))
                    else:
                        return 1
                else:
                    comp = 0

        for i in range(0, 9):
            testlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0, 9):
                if self.data[j][i]:
                    if int(self.data[j][i]) in testlist:
                        testlist.remove(int(self.data[j][i]))
                    else:
                        return 1
                else:
                    comp = 0

        for i in range(0, 9):
            testlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for j in range(0, 9):
                if self.data[3 * (i / 3) + (j / 3)][3 * (i / 3) + (j % 3)]:
                    if int(self.data[3 * (i / 3) + (j / 3)]
                           [3 * (i / 3) + (j % 3)]) in testlist:
                        testlist.remove(
                            int(self.data[3 * (i / 3) + (j / 3)][3 * (i / 3) + (j % 3)]))
                    else:
                        return 1
                else:
                    comp = 0
        if comp:
            return 2

        return 0


if __name__ == '__main__':
    data = [
        [
            8, 0, 3, 2, 0, 0, 7, 0, 0], [
            0, 0, 0, 0, 0, 6, 0, 0, 0], [
                0, 0, 0, 0, 0, 0, 0, 2, 0], [
                    0, 7, 2, 1, 0, 0, 0, 6, 0], [
                        0, 4, 0, 9, 7, 0, 0, 5, 0], [
                            0, 0, 0, 0, 0, 0, 0, 0, 0], [
                                0, 0, 9, 0, 0, 0, 2, 4, 0], [
                                    0, 0, 7, 0, 0, 4, 0, 9, 3], [
                                        1, 8, 0, 0, 0, 0, 5, 0, 0]]
    sud = Sudoku(data)
    print sud.complete
    print sud.duration
    print sud.data
