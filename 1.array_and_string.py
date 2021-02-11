
class ArrayAndString(object):
    # 1.1 문자열에 포함된 문자들이 전부 유일한지를 검사하는 알고리즘을 구현하라.
    # 다른 자료구조를 사용할 수 없는 상황이라면 어떻게 하겠는가?
    # --해결--
    # for 문을 통해 문자를 하나씩 검사
    # 답지의 다른 방안
    # 1. boolean 배열을 사용하여 문자열을 인덱스로 접근하여 중복 판단
    # 2. 정렬후 인접한 문자가 중복인지 판단
    @staticmethod
    def _1_is_unique_str(string):
        if len(string) > 256:   # ascii 의 경우 1바이트를 사용하므로 이를 초과한 문자열의 경우 중복이 있음.
            return False
        for i, s in enumerate(string):
            if s in string[i+1:]:
                return False
        return True

    def is_unique_str_execute(self):
        string = "a231gs"
        string2 = "ab2fasw2"
        for param in [string, string2]:
            if self._1_is_unique_str(param):
                print("Unique!")
            else:
                print("Not Unique!!")

    # 1.2 NULL 문자로 끝나는 문자열을 뒤집는 reverse(char* str) 함수를 C나 C++로 구현하라. (파이썬으로 하였음)
    # --해결--
    # 파이썬은 간단하게 step = -1로 구현 가능
    @staticmethod
    def _2_reverse_str(string):
        return ''.join(string[::-1])

    def reverse_str_execute(self):
        string = "123456789"
        string2 = "abcdefghijklmnopqrstuvwxyz"
        for s in [string, string2]:
            print(self._2_reverse_str(s))

    # 1.3 문자열 2개를 입력으로 받아 그중 하나가 다른 하나의 순열인지 판별하는 메서드를 작성하라
    # --해결--
    # 정렬하여 두 문자가 같으면 순열
    @staticmethod
    def _3_is_permutation(string1, string2):
        return True if sorted(string1) == sorted(string2) else False

    def is_permutation(self):
        string1 = "abcdedf"
        string1_2 = "abde"
        string2 = "12345"
        string2_2 = "54213"
        print(self._3_is_permutation(string1, string1_2))
        print(self._3_is_permutation(string2, string2_2))

    # 1.4 주어진 문자열 내의 모든 공백을 '%20'으로 바꾸는 메서드를 작성하라.
    # 문자열 끝에 추가로 필요한 문자들을 더할 수 있는 충분한 공간이 있다고 가정하라.
    # 그리고 공백을 포함하는 문자열의 길이도 함께 주어진다고 가정하라
    # (주의: Java로 구현한다면, 문자 배열을 사용하여 필요한 연산을 각 문자에 바로 적용할 수 있도록 하라.)
    # -예
    # 입력: "Mr John Smith    "
    # 출력: "Mr%20Jhon%20Smith"
    # --해결--
    # 뒤에서 부터 문자열을 체크 후 공백이면 %20으로 변환 후 문자열을 뒤집음
    @staticmethod
    def _4_replace_empty_space(string):
        is_end_char = False
        reversed_array = []
        for s in string[::-1]:
            if not is_end_char and s != ' ':
                reversed_array.append(s)
                is_end_char = True
            elif is_end_char:
                if s == ' ':
                    reversed_array.append('%20')
                else:
                    reversed_array.append(s)
        return ''.join(reversed(reversed_array))

    def replace_empty_space(self):
        string = "Mr John Smith    "
        print(string)
        for s in [string]:
            print(self._4_replace_empty_space(s))

    # 1.5 같은 문자가 연속으로 반복될 경우, 그 횟수를 사용해 문자열을 압축하는 메서드를 구현하라.
    # 가령 압축해야 할 문자열이 aabccccccccaaa라면 a2b1c8a3과 같이 압축되어야 한다.
    # 압축 결과로 만들어지는 문자열이 원래 문자열 보다 짧아지지 않는 경우, 이 메서드는 원래 문자열을 그대로 반환해야 한다.
    @staticmethod
    def _5_compress_str(string):
        compressed_string = []
        prev_string = string[0]
        prev_count = 1
        for s in string[1:]:
            if prev_string != s:
                compressed_string.append(prev_string)
                compressed_string.append(str(prev_count))
                prev_string = s
                prev_count = 1
            else:
                prev_count += 1
        compressed_string += prev_string + str(prev_count)
        compressed_string = ''.join(compressed_string)
        return compressed_string if len(string) > len(compressed_string) else string

    def compress_str(self):
        string = "aabccccccccaa"
        string2 = "abcdefg"
        for s in [string, string2]:
            print(self._5_compress_str(s))


if __name__ == '__main__':
    q = ArrayAndString()
    q.compress_str()
