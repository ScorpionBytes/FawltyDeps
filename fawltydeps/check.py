"Compare imports and dependencies"

from typing import List, Tuple, Set
import isort


def compare_imports_to_dependencies(
    imports: List[str], dependencies: List[str]
) -> Tuple[Set[str], Set[str]]:
    """
    Compares imports to dependencies

    Returns set of undeclared non stdlib imports and set of unused dependencies
    """
    non_stdlib_imports = {
        module for module in imports if isort.place_module(module) != "STDLIB"
    }
    undeclared = set(non_stdlib_imports) - set(dependencies)
    unused = set(dependencies) - set(non_stdlib_imports)
    return undeclared, unused
