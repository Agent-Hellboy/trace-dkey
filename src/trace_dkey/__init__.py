import _ast
import ast
from typing import Tuple, List, Any, Dict


def __process_tuple(tuple_elts: List) -> Tuple:
    ans = []
    for elt in tuple_elts:
        ans.append(elt.value)
    return tuple(ans)


def __trace_key(dict_key: Any, dict_value: Any, key, response: str) -> None:
    if type(dict_key) == _ast.Constant:
        if dict_key.value == key:
            print(f"Found '{key}' at {response[3:]+'-->'+key}")
        else:
            response += f"--> {dict_key.value}"
            if type(dict_value) == _ast.Dict:
                for i in range(len(dict_value.keys)):
                    __trace_key(dict_value.keys[i], dict_value.values[i], key, response)
    if type(dict_key) == _ast.Tuple:
        tuple_key = __process_tuple(dict_key.elts)
        response += "-->" + str(tuple_key)
        if type(dict_value) == _ast.Dict:
            for i in range(len(dict_value.keys)):
                __trace_key(dict_value.keys[i], dict_value.values[i], key, response)


def trace(dictionary: Dict, key: Any) -> None:
    dict_expr = str(dictionary)
    ast_obj = ast.parse(dict_expr, mode="eval")
    for indx in range(len(ast_obj.body.keys)):
        __trace_key(ast_obj.body.keys[indx], ast_obj.body.values[indx], key, "")
