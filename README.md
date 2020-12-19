<h1>Nspire-Library</h1>

TI-Nspire programs library

<h1>Xcalc</h1>

Calculus & utilities library


<h2>Public Functions</h2>


### **def(expr)**

Domain of *expr*

Stores result in global variable <ins>def_val</ins>

Stores full result in global variable <ins>def_val_raw</ins>


### **def_info(expr, print)**

Domain analysis of *expr* and derivative of *expr*

Displays info if *print* is `true`

Stores whether the domains are equal in global variable <ins>def_match</ins>


### **def_print(expr)**

Same as **def(expr)** but prints out <ins>def_val</ins> and <ins>def_val_raw</ins> 


### **range(function)**

Range of *function*


### **fn_info(function)**

Analysis of *function*


### **inverse(function)**

Inverse function of *function*


### **rational_fn(num, den)**

Rational function analysis 

(where P is *num* and Q is *den*)


### **crit_points(function)**

Critical points of *function*

Displays f'(x) and roots of f'(x)

Displays 2 domains of f(x) and f'(x)


### **inflect_points(function)**

Inflection points of *function*

Displays f''(x) and roots of f''(x)

Displays domain of f''(x)


### **parity(function, out_value)**

Parity of *function* (even/odd/neither)

Stores result in variable with name *out_value*


### **antiderivative(function, variable)**

Antiderivative of *function* with respect to *variable*


### **syndiv(poly, div)**

Synthetic division of *poly* by *div*

Returns a list of the coefficients with the last element
the remainder


### **bernoulli(m)**

Returns Bernoulli number *m* (for *m*>0)



<h2>Utility Functions</h2>


### **str_contains(str, find)**

String contains function

Determines whether *str* contains substring *find*


### **str_list(str)**

Converts *str* to a list

Stores result in global variable <ins>szlist_val</ins>


### **list_str(list)**

Converts *list* to a string

Stores result in global variable <ins>rgstr_val</ins>


### **char_at(str, i)**
Returns the char (as string) at *i* in *str*


### **parse_fn(function)**

Stores *function* into f(x)



<h2>Internal Functions</h2>

**get_undef(expr)**

Parses the values where x is undefined from the expression (WIP)


**add_item(list, element)**

Adds element to *list* and returns the modified *list*


**filter_cplx(list)**

Removes all imaginary/complex values of *list*

Stores result in global variable <ins>filter_val</ins>


**safe_bool(value)**

Returns `false` if *value* is not a boolean

Otherwise it returns *value*



# Reference

[Wiki](https://github.com/Decimation/Nspire-Library/wiki)

[Useful Reference](https://github.com/Decimation/Nspire-Library/wiki/Useful-Reference)
