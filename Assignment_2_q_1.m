nodes=randi(100,1,1);
iters=input("Enter no. of interations:");
w=randn(nodes,iters);
neighbours=randi([0,1],nodes,nodes);
for i=1:nodes
    for j=1:i
        neighbours(i,j)=neighbours(j,i);
        if(j==i)
            neighbours(i,j)=0;
        end
            
    end
end

