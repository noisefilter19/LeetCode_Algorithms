#include<stdio.h>
#include<stdlib.h>
struct poly
{	int coeff,exp;
	struct poly *next;
};
void display(struct poly *start)
{  if(start==NULL)
  printf("LL is Empty");
  else
  {struct poly *temp;
  temp=start;
  while(temp->next!=NULL)
  {printf("%dx^%d+",temp->coeff,temp->exp);
  temp=temp->next;   }
  printf("%dx^%d",temp->coeff,temp->exp);  }
}
struct poly * create(int c,int e,struct poly *start)
{	struct poly *newn=(struct poly*)malloc(sizeof(struct poly));
	struct poly *temp=start;
	newn->coeff=c;
	newn->exp=e;
	if(start==NULL)
	{start=newn;
	 start->next=NULL;  }
	else
	{while(temp->next!=NULL)
		temp=temp->next;
	temp->next=newn;
	temp=newn;
	temp->next=NULL;  }
	return start;
}
void multiply(struct poly *pptr,struct poly *qptr)
{	struct poly *temp,*prev=NULL,*temp1,*temp2,*t;
	struct poly  *iptr=(struct poly*)malloc(sizeof(struct poly));
	struct poly *fr=(struct poly*)malloc(sizeof(struct poly));
	iptr=NULL;
	fr=NULL;
	int c,e,f=0;
	for(temp1=pptr;temp1!=NULL;temp1=temp1->next)
		for(temp2=qptr;temp2!=NULL;temp2=temp2->next)
		{	c=temp1->coeff*temp2->coeff;
		 	e=temp1->exp+temp2->exp;
		 	iptr=create(c,e,iptr);  }
	display(iptr);
	printf("\nFinal Answer\n");
	for(temp=iptr;temp!=NULL;temp=temp->next)
	{	f=0;
		prev=temp;
		t=temp->next;
		c=temp->coeff;
		e=temp->exp;
		for(prev=temp,t=temp->next;t!=NULL;t=t->next)
		{	if(temp->exp==t->exp)
			{	c=c+t->coeff;
			 	prev->next=t->next;    }
			prev=prev->next;  }
		fr=create(c,e,fr);        }
	display(fr);
}
void add(struct poly *pptr,struct poly *qptr)
{	struct poly *rptr=(struct poly*)malloc(sizeof(struct poly));
	rptr=NULL;
	int c,e;
	while(pptr!=NULL && qptr!=NULL)
	{	if(pptr->exp==qptr->exp)
		{	e=pptr->exp;
			c=pptr->coeff+qptr->coeff;
			rptr=create(c,e,rptr);
			pptr=pptr->next;
			qptr=qptr->next;       }
		else if(pptr->exp>qptr->exp)
		{	e=pptr->exp;
			c=pptr->coeff;
			rptr=create(c,e,rptr);
			pptr=pptr->next;       }
		else
		{	e=qptr->exp;
			c=qptr->coeff;
			rptr=create(c,e,rptr);
			qptr=qptr->next;       }
	}
	while(pptr!=NULL)
	{	e=pptr->exp;
		c=pptr->coeff;
		rptr=create(c,e,rptr);
		pptr=pptr->next;           }
	while(qptr!=NULL)
	{	e=qptr->exp;
		c=qptr->coeff;
		rptr=create(c,e,rptr);
		qptr=qptr->next;          }
	display(rptr);
}
void main()
{	int u,c,e,ch;
	struct poly *p=(struct poly*)malloc(sizeof(struct poly));
	struct poly *q=(struct poly*)malloc(sizeof(struct poly));
	p=NULL;
	q=NULL;
	printf("\nEnter the 1st polynomial:");
	do
	{printf("\nEnter the coefficient:");
	scanf("%d",&c);
	printf("\nEnter the exponent:");
	scanf("%d",&e);
	p=create(c,e,p);
	printf("\nDo you want to continue:[1/0]");
	scanf("%d",&u);
	}while(u==1);
	printf("\nEnter the 2st polynomial:");
	do{
	printf("\nEnter the coefficient:");
	scanf("%d",&c);
	printf("\nEnter the exponent:");
	scanf("%d",&e);
	q=create(c,e,q);
	printf("\nDo you want to continue:[1/0]");
	scanf("%d",&u);
	}while(u==1);
	printf("\nExp1:");
	display(p);
	printf("\nExp2:");
	display(q);
	do{
	printf("\n\tMenu\n");
	printf("1.Addition\n2.Multiplication\n3.Exit");
	printf("\nEnter your choice:");
	scanf("%d",&ch);
	if(ch==1)
	{add(p,q);}
	else if(ch==2)
	{multiply(p,q); }
	}while(ch<3);
}			
