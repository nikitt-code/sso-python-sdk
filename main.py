from ssosdk import SSOSDK

if __name__ == '__main__':
    app = SSOSDK("TOKEN HERE")

    # users.get
    # users_array - array of ids, if u need one user [ id ]
    # app.usersGet([ 463406970 ])

    # transfer.create
    # id - recipient id, count - value of send coins
    # app.transfersCreate(id, count)

    # transfers.getHistory
    # count - count of transfers to show
    # app.transfersGetHistory(count)

    # transfers.get
    # transfer_ids - array of ids of transfers, if u need one transfer [ id ]
    # app.transfersGet([ 743 ])

    # webhooks.get
    # app.webhooksGet(url)

    # webhooks.create
    # url - url to your server
    # app.webhooksSet(url)

    # webhooks.delete
    # app.webhooksDelete(url)

    # promocodes.create
    # count, activations
    # app.promoCreate(count, activations)

    # promocodes.get
    # app.promoGet()

    # promocodes.activate
    # code - promocode value
    # app.promoActivate()