grammar punto5;

expr: expr op=('+'|'-') expr  # AddSub
    | expr op=('*'|'/') expr  # MulDiv
    | complexNumber           # ComplexNum
    | '(' expr ')'            # Parens
    ;

complexNumber: SIGN? NUMBER ('+'|'-')? NUMBER? 'i'?;

NUMBER: [0-9]+ ('.' [0-9]+)?;
SIGN: ('+'|'-');
WS: [ \t\r\n]+ -> skip;
