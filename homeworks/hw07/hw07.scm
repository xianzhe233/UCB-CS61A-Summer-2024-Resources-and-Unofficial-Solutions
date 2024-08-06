(define (add-leaf t x)
  (if (is-leaf t)
      t
      (begin (define mapped-branches
                     (map (lambda (b) (add-leaf b x)) (branches t)))
             (tree (label t)
                   (append mapped-branches (tree (tree x nil) nil))))))
