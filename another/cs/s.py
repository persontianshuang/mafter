def permutation(k,m):
    if k==m:

for(i=0;i<=m;i++)
cout<<a[i];
cout<<endl;
}
else
{
for(j=k;j<=m;j++)
{
swap(a[j],a[k]);
permutation(a,k+1,m);
swap(a[j],a[k]);
}
}
}
int main(void)
{
    char a[] = "abc";
cout<<a<<"所有全排列的结果为："<<endl;
permutation(a,0,2);
system("pause");
return 0;
}
