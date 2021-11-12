const PI = 3.14;
//writing "PI = 42" on the following line will now throw an error.
//This is because variables declared with const cannot be be redeclared in the same scope.

//The difference between var and let are that var can be hoisted and used even if it is written last in its scope, whereas let will not allow you to use it before it is declared. Another difference is that you cannot redeclare a variable made using let while var you can redeclare. A similarity between let and var is that you can mutate and set new values.

//The difference between var and const is the same for the hoisting situation as let and var. Objects and arrays made with const are MUTABLE but you cannot set it to a different value, whereas var allows you to redeclare, set new values, and perform operations on the value. Any primitive data type declared with const will not be changeable.

//The only difference between let and const is that where let allows us to modify its values, such as incrementing and setting to new values entirely, const will not permit that. Both are mutable in the same situations and are not hoisted, as opposed to var.