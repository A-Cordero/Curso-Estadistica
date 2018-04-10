#Nombre : Anthony Ariano Cordero Gavilan 20120434B
#Respuesta 2 : El codigo muestra el uso , manipulacion y creacion de matrices en R

#a)
mymat1 = matrix( data = c( 4.3, 3.1, 8.2, 8.2, 3.2, 0.9, 1.6, 6.5 ), nrow = 4, ncol = 2, byrow = TRUE)
#b)
dim( mymat1[-1,])
#c)
mymat1[,2] = sort( mymat1[,2], decreasing = FALSE)
mymat1
#d)
mymat2 = matrix( data = mymat1[-4, -1])
dim( mymat2)
#e)
mymat3 = matrix( data = mymat1[ 3:4, 1:2], nrow = 2, ncol =2)
mymat3
#f)
mymat1[ c(4,1), 2:1] <- (-1/2)*diag(mymat3)
mymat1
#g)
A = matrix( data = c(0) , nrow = 4, ncol = 4)
diag( x = A) <- c( 2, 3, 5, -1)
A_2 = solve(A)%*%A - diag( x = 4)
A_2
