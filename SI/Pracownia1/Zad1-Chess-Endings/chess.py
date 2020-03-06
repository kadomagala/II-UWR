import queue

DEBUG = True


class ChessModel:
    def __init__(self, color, w_king_pos, w_rook_pos, b_king_pos):
        self.color = color
        self.w_king_pos = w_king_pos
        self.w_rook_pos = w_rook_pos
        self.b_king_pos = b_king_pos

    def possible_moves(self, state):
        result = []
        wk_pos = state[1]
        rk_pos = state[2]
        bk_pos = state[3]
        if state[0] == 'black':
            # only black king move
            for x in range(-1, 2):
                for y in range(-1, 2):
                    new_pos = ""
                    new_pos += chr(x + ord(bk_pos[0])) + chr(y + ord(bk_pos[1]))
                    if self.is_correct_pos(new_pos):
                        result.append(['white', wk_pos, rk_pos, new_pos])
        else:
            # white king moves
            for x in range(-1, 2):
                for y in range(-1, 2):
                    new_pos = ""
                    new_pos += chr(x + ord(wk_pos[0])) + chr(y + ord(wk_pos[1]))
                    if self.is_correct_pos(new_pos):
                        result.append(['black', new_pos, rk_pos, bk_pos])
            # white rook moves
            for x in range(ord(rk_pos[0])-1, ord('a') - 1, -1):
                new_pos = ""
                new_pos += chr(x) + rk_pos[1]
                if self.is_correct_pos(new_pos):
                    result.append(['black', wk_pos, new_pos, bk_pos])

            for x in range(ord(rk_pos[0])+1, ord('h') + 1):
                new_pos = ""
                new_pos += chr(x) + rk_pos[1]
                if self.is_correct_pos(new_pos):
                    result.append(['black', wk_pos, new_pos, bk_pos])

            for x in range(ord(rk_pos[1])-1, ord('1') - 1, -1):
                new_pos = ""
                new_pos += rk_pos[0] + chr(x)
                if self.is_correct_pos(new_pos):
                    result.append(['black', wk_pos, new_pos, bk_pos])
            for x in range(ord(rk_pos[1])+1, ord('8') + 1):
                new_pos = ""
                new_pos += rk_pos[0] + chr(x)
                if self.is_correct_pos(new_pos):
                    result.append(['black', wk_pos, new_pos, bk_pos])

        return result

    @staticmethod
    def is_correct_pos(pos):
        return 'a' <= pos[0] <= 'h' and '1' <= pos[1] <= '8'

    @staticmethod
    def is_end_state(state):
        if state[0] == 'white':
            return False
        wk_pos = state[1]
        rk_pos = state[2]
        bk_pos = state[3]

        if bk_pos[0] == 'a':
            if bk_pos[1] == '1':
                if rk_pos[0] == 'a' and rk_pos[1] > '2' and wk_pos == 'c2':
                    return True
                elif rk_pos[1] == '1' and rk_pos[0] > 'b' and wk_pos == 'b3':
                    return True
                else:
                    return False
            elif bk_pos[1] == '8':
                if rk_pos[0] == 'a' and rk_pos[1] < '7' and wk_pos == 'c7':
                    return True
                elif rk_pos[1] == '8' and rk_pos[0] > 'b' and wk_pos == 'b6':
                    return True
                else:
                    return False
            else:
                return wk_pos[0] == 'c' and wk_pos[1] == bk_pos[1] and rk_pos[0] == bk_pos[0] and abs(ord(bk_pos[1]) - ord(rk_pos[1])) > 1
        elif bk_pos[0] == 'h':
            if bk_pos[1] == '1':
                if rk_pos[0] == 'h' and rk_pos[1] > '2' and wk_pos == 'f2':
                    return True
                elif rk_pos[1] == '1' and rk_pos[0] < 'g' and wk_pos == 'g3':
                    return True
                else:
                    return False
            elif bk_pos[1] == '8':
                if rk_pos[0] == 'h' and rk_pos[1] < '7' and wk_pos == 'f7':
                    return True
                elif rk_pos[1] == '8' and rk_pos[0] > 'b' and wk_pos == 'g6':
                    return True
                else:
                    return False
            else:
                return wk_pos[0] == 'f' and wk_pos[1] == bk_pos[1] and rk_pos[0] == bk_pos[0] and abs(ord(bk_pos[1]) - ord(rk_pos[1])) > 1

        elif bk_pos[1] == '1':
            return wk_pos[1] == '3' and wk_pos[0] == bk_pos[0] and rk_pos[1] == bk_pos[1] and abs(ord(bk_pos[0]) - ord(rk_pos[0])) > 1

        elif bk_pos[1] == '8':
            return wk_pos[1] == '6' and wk_pos[0] == bk_pos[0] and rk_pos[1] == bk_pos[1] and abs(ord(bk_pos[0]) - ord(rk_pos[0])) > 1
        else:
            return False

    def get_initial_state(self):
        return [self.color, self.w_king_pos, self.w_rook_pos, self.b_king_pos]


def bfs(model):
    q = queue.Queue()
    visited = set()
    state = model.get_initial_state()

    if DEBUG:
        q.put([0, state, [state]])
    else:
        q.put([0, state])

    while not q.empty():
        state = q.get()
        if model.is_end_state(state[1]):
            if DEBUG:
                return state
            else:
                return state[0]
        else:
            visited.add(tuple(state[1]))
            for move in model.possible_moves(state[1]):
                if tuple(move) not in visited:
                    #print(move)
                    if DEBUG:
                        q.put([state[0] + 1, move])#, state[2].copy().append(move)])
                    else:
                        q.put([state[0] + 1, move])


modl = ChessModel('black', 'b4', 'f3', 'e8')

print(bfs(modl))
