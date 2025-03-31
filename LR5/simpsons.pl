% Пол
male(homer).
male(bart).
male(abraham).
male(clancy).
male(herb).

female(marge).
female(lisa).
female(maggie).
female(jackie).
female(patty).
female(selma).
female(mona).
female(ling).

% Родители
parent(homer, bart).
parent(homer, lisa).
parent(homer, maggie).

parent(marge, bart).
parent(marge, lisa).
parent(marge, maggie).

parent(clancy, marge).
parent(clancy, patty).
parent(clancy, selma).

parent(jacqueline, marge).
parent(jacqueline, patty).
parent(jacqueline, selma).

parent(abraham, homer).
parent(mona, homer).

parent(selma, ling).

% Брак
married(homer, marge).
married(clancy, jackie).

husband(X, Y) :- parent(X, Z), parent(Y, Z), male(X).
wife(X, Y) :- parent(X, Z), parent(Y, Z), female(X).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

grandfather(X, Y) :- parent(Z, Y), father(X, Z).
grandmother(X, Y) :- parent(Z, Y), mother(X, Z).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).

uncle(X, Y) :- sibling(X, Z), parent(Z, Y), male(X).
aunt(X, Y) :- sibling(X, Z), parent(Z, Y), female(X).

nephew(X, Y) :- sibling(Y, Z), parent(Z, X), male(X).
niece(X, Y) :- sibling(Y, Z), parent(Z, X), female(X).

mother_in_law(X, Y) :- married(Y, Z), mother(X, Z).
father_in_law(X, Y) :- married(Y, Z), father(X, Z).

% Правило для поиска всех людей
person(X) :- male(X); female(X).

% Правило для поиска людей без детей
no_children(X) :- person(X), \+ parent(X, _).
