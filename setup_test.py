import unittest
import coverage


if __name__ == "__main__":
    code_coverage = coverage.Coverage()
    code_coverage.start()

    unittest_loader = unittest.TestLoader()
    suite = unittest_loader.discover(start_dir=".", pattern="*_test.py")
    tests_runner = unittest.TextTestRunner(verbosity=3)
    tests_runner.run(suite)

    code_coverage.stop()
    code_coverage.save()
    code_coverage.html_report(directory="code_coverage")
