(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (list keys values)  
)

(define (get-keys-kwlist1 kwlist)
  (car kwlist)
)

(define (get-values-kwlist1 kwlist)
  (cadr kwlist)  
)

(define (make-kwlist2 keys values)
  (if (or (null? keys) (null? values))
    nil
    (cons (list (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))
  )  
)

(define (get-keys-kwlist2 kwlist)
  (define (get_first lst) (car lst))
  (map get_first kwlist)
)

(define (get-values-kwlist2 kwlist)
  (define (get_second lst) (cadr lst))
  (map get_second kwlist)
)

(define (add-to-kwlist kwlist key value)
  (make-kwlist (append (get-keys-kwlist kwlist) (list key)) (append (get-values-kwlist kwlist) (list value)))
)

(define (get-first-from-kwlist kwlist key)
  (let 
    ((keys (get-keys-kwlist kwlist))
      (values (get-values-kwlist kwlist))
    )
    (define (find-value keys values)
      (if (null? keys)
          '()
          (if (equal? (car keys) key)
              (car values)
              (find-value (cdr keys) (cdr values)))) 
    )
    (find-value keys values)
  )
)
