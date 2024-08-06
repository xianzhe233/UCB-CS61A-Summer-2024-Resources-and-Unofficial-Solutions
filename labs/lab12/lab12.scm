(define (no-repeats s)
  (if (null? s)
    nil
    (cons (car s) (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s))))
  )
)

(define (without-duplicates lst) (no-repeats lst))

(define (reverse lst)
  (if (null? lst)
    nil
    (append (reverse (cdr lst)) (list (car lst)))
  )
)
