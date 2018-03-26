nodes=randi(10,1,1);
iters=input('Enter no. of iterations:');
w=randn(nodes,iters);
u=randn(nodes,iters);
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






