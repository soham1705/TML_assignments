nodes=randi(10,1,1);
iters=input('Enter no. of iterations:');
w=randn(nodes,iters);
u=randn(nodes,iters);
mu=0.01;
neighbours=randi([0,1],nodes,nodes);

for i=1:nodes
    for j=1:i
        neighbours(i,j)=neighbours(j,i);
        if(j==i)
            neighbours(i,j)=0;
        end
    end
end

a=neighbours;
for i=1:nodes
    sum=0;
    for j=1:nodes
        sum=sum+neighbours(i,j);
    end
    for j=1:nodes
        a(i,j)=neighbours(i,j)/sum;
    end
end

c=a;
d=randi([0,1],nodes,1);

psi=zeros(nodes,iters);

for k=1:nodes
    for i=1:iters
        neighbour_sum=0;
        for l=1:nodes
            if(neighbours(k,l)==1)
                if(i>1)
                    neighbour_sum=neighbour_sum+c(l,k)*u(l,i)*(d(l)-u(l,i)*w(k,i-1));
                elseif(i==1)
                     neighbour_sum=neighbour_sum;
                end
            end
        end
        if(i>1)
            psi(k,i)=w(k,i-1)+mu*neighbour_sum;
        elseif(i==1)
            psi=mu*neighbour_sum;
        end
        a_psi_sum=0;
        for l=1:nodes
            if(neighbours(k,l)==1)
                a_psi_sum=a_psi_sum+a(l,k)*psi(l,i);
            end
        end
        w(k,i)=a_psi_sum;
    end
end

    






