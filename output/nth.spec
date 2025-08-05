(*generated using Prudent *) 

 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )  y ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  l1 )   ( init  l2 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a11  ( goal   ( last  l1 )  a1 a3 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  y )   ( goal  a2 a2 y )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  y )   ( goal   ( last  l1 )  a2 l2 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take  a11  ( goal  a2 size l1 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  l2 )   ( goal  ep  ( last  y )  l2 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  l1 )  l1 ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  l1 )   ( goal  a11  ( last  a3 )   ( init  a3 )  )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  l1 )   ( goal  size a1 l2 )  ) 
 (* Program *) 
let rec goal    (a1 : int)  (a2 : int)  (a3 : Ty_list int) : (Ty_list int) = 
 	  ( take   ( last  a3 )   ( goal  a11  ( last  a3 )   ( init  a3 )  )  ) 
