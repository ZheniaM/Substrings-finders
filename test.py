from typing import Callable
import unittest
import time
import traceback
from threading import Timer
from substring_finders._automaton import automaton
from substring_finders._a_c import apostolico_crocemor
from substring_finders._bauler_mure import bauler_mure
from substring_finders._boyer_moore_horspool import boyer_moore_horspool
from substring_finders._bruteforce import bruteforce
from substring_finders._knuth_morris_pratt import knuth_morris_pratt
from substring_finders._rabin_carp import rabin_carp
from substring_finders._suffix_tree_substr import suffix_tree_substr
from substring_finders._z_func import z_func


class FindersTest(unittest.TestCase):
    targets: dict[str, int] = {
        "Lovecraft": 107,
        "I am": 7,
        "other field than this": 1,
        "possible": 24
    }

    def setUp(self) -> None:
        with open("file.txt") as file:
            self.__text: str = file.read()

    def find_with_timeout(self,
                          finder: Callable,
                          source: str, target: str,
                          timeout: int = 3) -> list[int]:
        def timeout_handler():
            raise TimeoutError("timeout exceeded for " +
                               f"{finder.__name__} for {timeout} sec")

        timer: Timer = Timer(timeout, timeout_handler)
        timer.start()
        result: list[int] = []

        try:
            start_time: float = time.time()
            result = finder(source, target)
            end_time: float = time.time()
            t: str = f"'{target}'"
            print(f"{finder.__name__:<15}for target = {t:<25}" +
                  f"\ttook\t{end_time - start_time:6.4f}")
        except TimeoutError:
            ...
        except Exception:
            print(traceback.format_exc())
        finally:
            timer.cancel()
            return result

    def test_automaton_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(automaton, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_apostolico_crocemor_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(
                apostolico_crocemor, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_bauler_mure_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(bauler_mure, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_boyer_moore_horspool_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(
                boyer_moore_horspool, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_bruteforce_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(bruteforce, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_knuth_morris_pratt_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(
                knuth_morris_pratt, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_rabin_carp_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(rabin_carp, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_suffix_tree_substr_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(
                suffix_tree_substr, self.__text, target)
            self.assertEqual(expected_len, len(result))

    def test_z_func_working(self):
        print()
        for target, expected_len in self.targets.items():
            result = self.find_with_timeout(z_func, self.__text, target)
            self.assertEqual(expected_len, len(result))


if __name__ == '__main__':
    unittest.main()
