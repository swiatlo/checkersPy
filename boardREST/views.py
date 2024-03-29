from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view # new
from checkers.boardREST.board import Board, m_side
from checkers.boardREST.scoredboard import ScoredBoard
from random import *
from . import serializers
from . import Task


# Global variable used for the sake of simplicity.
# In real life, you'll be using your own interface to a data store
# of some sort, being caching, NoSQL, LDAP, external API or anything else
tasks = {
    1: Task(id=1, name='Demo', owner='xordoquy', status='Done'),
    2: Task(id=2, name='Model less demo', owner='xordoquy', status='Ongoing'),
    3: Task(id=3, name='Sleep more', owner='xordoquy', status='New'),
}


def get_next_task_id():
    return max(tasks) + 1


class BoardViewSet(viewsets.ViewSet):
    serializer_class = serializers.BoardSerializer

    def retrieve(self, request, pk=None):
        try:
    #        task = tasks[int(pk)]
            #n=tasks[1]
           # print('pk ', pk)
           # print('rd ', request.data)

            sb = ScoredBoard(pk,[],Board('') ) # ' b    b bbbbbb w wwww www b     ')
            #sb.cacheRes = []
            #sb.compBoard = Board('')  
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        sb.computeMoves( 'b','w', m_side, 6)
        if len(sb.nextboards) ==0:
            return Response('game over')
            
 #       idx = randrange(0,len(sb.nextboards))
        xb = choice( [brd for brd in sb.tree if brd.pointValue == sb.pointValue] )

        #return Response(sb.nextboards[idx][0])
        serializer = serializers.BoardSerializer( xb )
        
        return Response(serializer.data)

    
    def list(self, request):
        return Response('lists')

#    def create(self, request):
 #       pass

  #  def update(self, request, pk=None):
   #     pass




class TaskViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.TaskSerializer

    def list(self, request):
        serializer = serializers.TaskSerializer(
            instance=tasks.values(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.id = get_next_task_id()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(instance=task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(
            data=request.data, instance=task)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.TaskSerializer(
            data=request.data,
            instance=task,
            partial=True)
        if serializer.is_valid():
            task = serializer.save()
            tasks[task.id] = task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            task = tasks[int(pk)]
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        del tasks[task.id]
        return Response(status=status.HTTP_204_NO_CONTENT)

