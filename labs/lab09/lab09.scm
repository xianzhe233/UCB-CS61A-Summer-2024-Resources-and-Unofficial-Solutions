(define (over-or-under num1 num2)
    	(cond ((< num1 num2) -1)
			  ((= num1 num2) 0)
			  (else 1)
		)
)

(define (make-adder num)
	(lambda (x) (+ x num))
)

(define (composed f g)
	(lambda (x) (f (g x)))
)

(define (repeat f n)
	(define (func x) 
		(if (= n 0)
			x 
			((repeat f (- n 1)) (f x))
		)	
	)
	func
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
	(define x (max a b))
	(define y (min a b))
	(if (= y 0)
		x
		(gcd y (modulo x y))
	)
)

(define (duplicate lst)
	(if (= (length lst) 0)
		nil
		(cons (car lst) (cons (car lst) (duplicate (cdr lst))))
	)
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s)
  	(if (null? s)
      	'()
      	(let 
			(
				(first  (if (list? (car s))
                       		(deep-map fn (car s))
                       		(fn (car s))
						)
				)
            	(rest (deep-map fn (cdr s)))
			)
        	(cons first rest)
		)
	)
)

