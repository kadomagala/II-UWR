import math
import queue

DEBUG = False


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
        dist_between_kings = self.dist_between_pieces(wk_pos, bk_pos)
        if state[0] == 'black':
            # only black king move
            for x in range(-1, 2):
                for y in range(-1, 2):
                    new_pos = ""
                    new_pos += chr(x + ord(bk_pos[0])) + chr(y + ord(bk_pos[1]))
                    if dist_between_kings > 2:
                        if self.dist_between_pieces(new_pos, wk_pos) > dist_between_kings:
                            continue
                    if new_pos == wk_pos \
                            or new_pos == rk_pos \
                            or self.is_enemy_king_nearby(new_pos, wk_pos) \
                            or self.rook_threatens_bking(new_pos, wk_pos, rk_pos) \
                            or new_pos == bk_pos:
                        continue
                    if self.is_correct_pos(new_pos):
                        result.append(('white', wk_pos, rk_pos, new_pos))
        else:
            # white king moves
            for x in range(-1, 2):
                for y in range(-1, 2):
                    new_pos = ""
                    new_pos += chr(x + ord(wk_pos[0])) + chr(y + ord(wk_pos[1]))
                    if dist_between_kings > 2:
                        if self.dist_between_pieces(new_pos, bk_pos) > dist_between_kings:
                            continue
                    if new_pos == bk_pos \
                            or new_pos == rk_pos \
                            or new_pos == wk_pos \
                            or self.is_enemy_king_nearby(new_pos, bk_pos):
                        continue
                    if self.is_correct_pos(new_pos):
                        result.append(('black', new_pos, rk_pos, bk_pos))
            # white rook moves

            candidate = "TT"
            for x in range(ord(rk_pos[0])-1, ord('a') - 1, -1):
                new_pos = ""
                new_pos += chr(x) + rk_pos[1]

                if new_pos == wk_pos \
                        or new_pos == bk_pos \
                        or self.is_enemy_king_nearby(bk_pos, new_pos):
                    break
                candidate = new_pos
            if self.is_correct_pos(candidate):
                result.append(('black', wk_pos, candidate, bk_pos))

            candidate = "TT"
            for x in range(ord(rk_pos[0])+1, ord('h') + 1):
                new_pos = ""
                new_pos += chr(x) + rk_pos[1]

                if new_pos == wk_pos \
                        or new_pos == bk_pos \
                        or self.is_enemy_king_nearby(bk_pos, new_pos):
                    break
                candidate = new_pos
            if self.is_correct_pos(candidate):
                result.append(('black', wk_pos, candidate, bk_pos))

            candidate = "TT"
            for x in range(ord(rk_pos[1])-1, ord('1') - 1, -1):
                new_pos = ""
                new_pos += rk_pos[0] + chr(x)

                if new_pos == wk_pos \
                        or new_pos == bk_pos \
                        or self.is_enemy_king_nearby(bk_pos, new_pos):
                    break
                candidate = new_pos
            if self.is_correct_pos(candidate):
                result.append(('black', wk_pos, candidate, bk_pos))

            candidate = "TT"
            for x in range(ord(rk_pos[1])+1, ord('8') + 1):
                new_pos = ""
                new_pos += rk_pos[0] + chr(x)

                if new_pos == wk_pos \
                        or new_pos == bk_pos \
                        or self.is_enemy_king_nearby(bk_pos, new_pos):
                    break
                candidate = new_pos
            if self.is_correct_pos(candidate):
                result.append(('black', wk_pos, candidate, bk_pos))
        return result

    @staticmethod
    def is_enemy_king_nearby(king1, piece):
        for x in range(-1, 2):
            for y in range(-1, 2):
                new_pos = ""
                new_pos += chr(x + ord(king1[0])) + chr(y + ord(king1[1]))
                if new_pos == piece:
                    return True
        return False

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
                return wk_pos[0] == 'c' \
                       and wk_pos[1] == bk_pos[1] \
                       and rk_pos[0] == bk_pos[0] \
                       and abs(ord(bk_pos[1]) - ord(rk_pos[1])) > 1
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
                return wk_pos[0] == 'f' \
                       and wk_pos[1] == bk_pos[1] \
                       and rk_pos[0] == bk_pos[0] \
                       and abs(ord(bk_pos[1]) - ord(rk_pos[1])) > 1

        elif bk_pos[1] == '1':
            return wk_pos[1] == '3' \
                   and wk_pos[0] == bk_pos[0] \
                   and rk_pos[1] == bk_pos[1] \
                   and abs(ord(bk_pos[0]) - ord(rk_pos[0])) > 1

        elif bk_pos[1] == '8':
            return wk_pos[1] == '6' \
                   and wk_pos[0] == bk_pos[0] \
                   and rk_pos[1] == bk_pos[1] \
                   and abs(ord(bk_pos[0]) - ord(rk_pos[0])) > 1
        else:
            return False

    def get_initial_state(self):
        return self.color, self.w_king_pos, self.w_rook_pos, self.b_king_pos

    @staticmethod
    def rook_threatens_bking(new_pos, wk_pos, rk_pos):
        for i in range(0, 2):
            if new_pos[i] == rk_pos[i]:
                if wk_pos[i] == new_pos[i]:
                    if new_pos[(i + 1) % 2] < wk_pos[(i + 1) % 2] < rk_pos[(i + 1) % 2] \
                            or rk_pos[(i + 1) % 2] < wk_pos[(i + 1) % 2] < new_pos[(i + 1) % 2]:
                        return False
                    else:
                        return True
                else:
                    return True
        return False

    @staticmethod
    def dist_between_pieces(piece1, piece2):
        c1 = ord(piece1[0]) - ord(piece2[0])
        c2 = ord(piece1[1]) - ord(piece2[1])
        return math.sqrt(c1*c1 + c2*c2)


def bfs(model):
    q = queue.Queue()
    visited = set()
    state = model.get_initial_state()
    if DEBUG:
        footprint = [state]
        q.put([0, state, footprint])
    else:
        q.put([0, state])

    while not q.empty():
        state = q.get()
        if model.is_end_state(state[1]):
            return state
        else:
            visited.add(state[1])
            for move in model.possible_moves(state[1]):
                if move not in visited:
                    if DEBUG:
                        new_footprint = state[2].copy()
                        new_footprint.append(move)
                        q.put([state[0] + 1, move, new_footprint])
                    else:
                        q.put([state[0] + 1, move])


if __name__ == '__main__':
    if DEBUG:
        t1 = ChessModel('black', 'g8', 'h1', 'c4')
        print(bfs(t1))

    else:
        with open('zad1_input.txt', 'r') as r:
            with open('zad1_output.txt', 'w') as w:
                for line in r:
                    s = line.split()
                    modl = ChessModel(s[0], s[1], s[2], s[3])
                    result = bfs(modl)
                    w.write(str(result[0]) + '\n')
