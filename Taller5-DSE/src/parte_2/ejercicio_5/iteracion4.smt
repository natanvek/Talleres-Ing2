(declare-const a Int)
(declare-const b Int)
(declare-const c Int)
(declare-const C1 Bool) 
(assert (= C1 (or (<= a 0) (or (<= b 0) (<= c 0)))))
(declare-const C2 Bool) 
(assert (= C2 (not (and (> (+ a b ) c) (and (> (+ a c ) b) (> (+ c b ) a)) ) )))
(declare-const C3 Bool) 
(assert (= C3 (and (= a b) (= b c))))
(declare-const C4 Bool) 
(assert (= C4 (or (= a b) (or (= b c) (= a c)))))

(assert (and (not C1) C2))
(get-model)