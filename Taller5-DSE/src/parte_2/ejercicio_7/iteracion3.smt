(declare-const n Int)

(declare-const i_0 Int)
(assert (= i_0 0))
(declare-const i_1 Int)
(assert (= i_1 1))
(declare-const i_2 Int)
(assert (= i_2 2))

(declare-const C1_0 Bool)
(assert (= C1_0 (< i_0 n)))
(declare-const C1_1 Bool)
(assert (= C1_1 (< i_1 n)))
(declare-const C1_2 Bool)
(assert (= C1_2 (< i_2 n)))
(assert (= C1_2 false)) ; porque el cuerpo del ciclo se puede ejecutar a lo sumo 2 veces

(assert (and C1_0 C1_1 C1_2))
(check-sat)
(get-model)