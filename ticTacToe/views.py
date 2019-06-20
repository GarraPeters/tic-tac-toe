from django.http import HttpResponse, JsonResponse
from . import game

def get_item(request):
    if len(request.GET.get('board')) == 9:
        board = request.GET.get('board')
        
        gameboard = game.Game(board)

        if gameboard.errMsg != '':
            response =  JsonResponse(
                {
                'status' : gameboard.errMsg
                },
            status=400)
        else:
            response = JsonResponse(
                {
                'status' : gameboard.status ,
                'board' : gameboard.gameString
                },
            status=200)

        return response

    else:
        return JsonResponse(
            {
            'status' : 'ERROR! Malformed game query'
            },
        status=400)
    return response
    