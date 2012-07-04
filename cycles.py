"""
R. Tarjan, Enumeration of the elementary circuits of a directed graph, SIAM Journal on Computing, 2 (1973), pp. 211-216

procedure circuit_enumeration;
  begin
    procedure BACKTRACK(integer value v, logical result f);
      begin
        logical g;
        f := false;
        place v on point stack;
        mark(v) := true;
        place v on marked stack;
        for w in A(v) do
          if w<s then delete w from A(v);
          else if w=s then
            begin
              output circuit from s to v to s given by point stack
              f:=true;
            end;
          else if not mark(w) then
            begin
              BACKTRACK(w,g);
              f:=f or g;
            end;
          comment f=true if an elementary circuit continuing the
            partial path on the stack has been found;
        if f=true then
          begin
            while top of marked stack is not v do
              begin
                u:=top of marked stack;
                delete u from marked stack;
                mark(u):=false
              end;
            delete v from marked stack;
            mar(v):=false;
          end;
        delete v from point stack;
      end;
    integer n;
    for i:=1 until v do mark(i):=false;
    for s:=1 until v do
      begin
        BACKTRACK(s,flag);
        while marked stack not empty do
          begin
            u:=top of marked stack;
            mark(u):=false;
            delete u from marked stack;
          end;
      end;
  end;
"""

import sys

if len(sys.argv) < 3:
    print "usage: %s num_vertices [v1,v2...]"%(sys.argv[0])

A = [[] for a in range(int(sys.argv[1]))]

for edge in sys.argv[2:]:
    v1,v2 = edge.split(',', 1)
    A[int(v1)].append(int(v2));

def print_point_stack():
    for p in point_stack:
        print p,
    print

point_stack = list()
marked = dict()
marked_stack = list()

def backtrack(v):
    f = False
    point_stack.append(v)
    marked[v] = True
    marked_stack.append(v)
    for w in A[v]:
        if w<s:
            A[w] = 0
        elif w==s:
            print_point_stack()
            f = True
        elif not marked[w]:
            f = backtrack(w) or f
    if f:
        while marked_stack[-1] != v:
            u = marked_stack.pop()
            marked[u] = False
        marked_stack.pop()
        marked[v] = False
    point_stack.pop()
    return f

for i in range(len(A)):
    marked[i] = False

for s in range(len(A)):
    backtrack(s)
    while marked_stack:
        u = marked_stack.pop()
        marked[u] = False
