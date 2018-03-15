% 1.a)
Aa=rand(200,20);
xa=rand(20,1);
ya=Aa*xa;

% 1.b)
Ab=rand(20,200);
xb=rand(200,1);
yb=Ab*xb;

% 2.a)
% Using normal equation

xa_obtained=inv(Aa'*Aa)*Aa'*ya;
norm(xa_obtained-xa);

% 2.b)
% Using normal equation

xb_obtained=pinv(Ab'*Ab)*(Ab'*yb);
norm(xb_obtained-xb);

% 3.a)

Aa_obtained=(ya*xa')*pinv(xa*xa');
norm(Aa_obtained-Aa)

% 3.b)

Ab_obtained=(yb*xb')*pinv(xb*xb');
norm(Ab_obtained-Ab)

% 4.

M=3;
N=5;
A=randn(M,M);
X=randn(M,N);
B=randn(N,N);
Y=randn(M,N);

F=kron(eye(N),A)+kron(B',eye(M));
vec_X_obtained=F\reshape(Y,M*N,1);
X_obtained=reshape(vec_X_obtained,M,N);
norm(X_obtained-X)
