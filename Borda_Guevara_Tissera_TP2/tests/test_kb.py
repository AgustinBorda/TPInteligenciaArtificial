from logic import FolKB
from utils import expr

kb = FolKB(map(expr, ['List(xs) ==> List(Ins(x, xs))',
                      'List(EmptyList)',
                      'Pert(x, Ins(x, xs))',
                      'Pert(x, ys) ==> Pert(x, Ins(y,ys))',
                      'Concat(EmptyList, ys, ys)',
                      'Concat(xs, ys, zs) ==> Concat(Ins(x, xs), ys, Ins(x, zs))']))


def test_list():
    assert repr(kb.ask(expr('List(EmptyList)'))) == '{}'
    assert repr(kb.ask(expr('List(Ins(One, EmptyList))'))) == '{v_3: One, v_2: EmptyList}'
    assert repr(kb.ask(expr('List(Ins(One, Ins(Two, EmptyList)))'))) == '{v_7: One, v_6: Ins(Two, EmptyList),' \
                                                                        ' v_9: Two, v_8: EmptyList}'
    assert repr(kb.ask(expr('List(Ins(One, Two))'))) == 'False'


def test_x_in_2_1_3():
    answer = kb.ask_generator(expr('Pert(x, (Ins(Two,Ins(One ,Ins(Three, EmptyList)))))'))
    for i in answer:
        if i == 0:
            assert i.x == 'Two'
        if i == 1:
            assert i.x == 'One'
        if i == 2:
            assert i.x == 'Three'


def test_2_in_1_x_3():
    answer = kb.ask_generator(expr('Pert(Two, (Ins(One,Ins(x ,Ins(Three, EmptyList)))))'))
    for i in answer:
        if i == 0:
            assert i.x == 'Two'


def test_x_y_concat_1_2_3():
    answer = kb.ask_generator(expr('Concat(x, y, Ins(One, Ins(Two, Ins(Three, EmptyList))))'))
    for i in answer:
        if i == 0:
            assert i.x == 'EmptyList' and i.y == 'Ins(One, Ins(Two, Ins(Three, EmptyList)))'  # x == [] & y == [1,2,3]
        if i == 1:
            assert i.x == 'Ins(One, EmptyList)' and i.y == 'Ins(Two, Ins(Three, EmptyList))'  # x == [1] & y == [2,3]
        if i == 2:
            assert i.x == 'Ins(Two, Ins(One, EmptyList))' and i.y == 'Ins(Three, EmptyList)'  # x == [1,2] & y == [3]
        if i == 3:
            assert i.x == 'Ins(Three, Ins(Two, Ins(One, EmptyList)))' and i.y == 'EmptyList'  # x == [1,2,3] & y == []
