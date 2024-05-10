(deftemplate animal (slot nombre))
(deftemplate carnivoro (slot nombre))

(defrule leon
    (animal (nombre leon))
    =>
    (assert (carnivoro (nombre leon))))

(defrule tigre
    (animal (nombre tigre))
    =>
    (assert (carnivoro (nombre tigre))))

(defrule come
    (carnivoro (nombre ?carnivoro))
    (animal (nombre ?presac))
    (not (carnivoro (nombre ?presac)))
    =>
    (printout t ?carnivoro " come " ?presac crlf))
