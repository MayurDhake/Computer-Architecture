.data

prompt1:
	.asciiz "\n Enter number 1 :"

prompt2:
	.asciiz "\n Enter number 2 :"

result1:
	.asciiz "\n The GCD is :"


Number1:
	.word 0

Number2:
	.word 0


.text

main:

#Read first number from user

li $v0,4
la $a0,prompt1
syscall

#Get input from keyboard

li $v0,5
syscall

#store word

sw $v0,Number1

#Read second number from user

li $v0,4
la $a0,prompt2
syscall

#Get input from keyboard

li $v0,5
syscall

#store word

sw $v0,Number2

#allocate stack

subu $sp,$sp,32
sw $ra,20($sp)
sw $fp,16($sp)
addiu $fp,$sp,28


#move to arguements

lw $a0,Number1
lw $a1,Number2
jal gcd



gcd:

subu $sp,$sp,32
sw $ra,20($sp)
sw $fp,16($sp)
addiu $fp,$sp,28
sw $a0,0($fp)
sw $a1,8($fp)

beq $a0,$a1,print_gcd
bgt $a0,$a1,greater
ble $a0,$a1,lesser

greater:

sub $v0,$a0,$a1
move $a0,$v0
jal gcd

lesser:

sub $v0,$a1,$a0
move $a1,$v0
jal gcd

print_gcd:

move $t0,$v0 		# copy gcd to t0


#print result

li $v0,4
la $a0,result1
syscall

li $v0,1
move $a0,$t0
syscall


li $v0,10
syscall
