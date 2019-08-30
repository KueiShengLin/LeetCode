class Solution:
    def convert(self, s: str, numRows: int) -> str:
        counter, revert_flag = 0, False
        rows = ["" for _ in range(numRows)]
        for s_char in s:
            rows[counter] += s_char
            
            if revert_flag is False:
                if counter < numRows - 1:
                    counter += 1
                elif counter == numRows - 1:
                    revert_flag = True
                    counter -= 1
            elif revert_flag:
                if counter > 0:
                    counter -= 1
                elif counter == 0:
                    revert_flag = False
                    counter += 1

        return "".join(rows)