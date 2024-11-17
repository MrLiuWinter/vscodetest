#根据最新价格确定下一轮报价
import copy
#报价函数
\
#根据最新价格确定下一轮报价
def bidding(current_assignment,current_prices):
    new_bid={}
    for bidder in bidder_set:
        if bidder in current_assignment:
            continue
        #未竞拍到物品的继续报价
        else:
            v_ij=[]
            available_object_list=copy.deepcopy(available_objects_for_bidders[bidder])
            for object in available_object_list:
                v_ij.append(value_matrix[bidder,object]-current_prices[object])
            max_v=max(v_ij) #最大收益
            bid_target=available_object_list[v_ij.index(max_v)] #最大收益对象
            v_ij.remove(max_v)
            available_object_list.remove(bid_target)
            sub_max_v=max(v_ij) #次大收益
            bid_price=value_matrix[bidder,bid_target]-sub_max_v+epsilon #下次报价
            if bid_target in new_bid:
                new_bid[bid_target][0].append(bidder)
                new_bid[bid_target][1].append(bid_price)
                print("dscsdf",new_bid)
            else:
                new_bid[bid_target]=[[bidder],[bid_price]]
                print("dscsdf", new_bid)
    return new_bid
#根据最新报价重新分配竞拍结果
def assigning(bid_prices,current_assignment,current_prices):
    new_prices={}
    for object in object_set:
        #收到报价的物品重新竞拍
        if object in bid_prices:
            bidders,prices=bid_prices[object]
            max_price=max(prices)
            bidder=bidders[prices.index(max_price)]
            new_prices[object]=max_price
            for people,object_ in current_assignment.items():
                if object_ == object:
                    current_assignment.pop(people)
                    current_assignment[bidder]=object
                    break
            if bidder not in current_assignment:
                current_assignment[bidder]=object
        else:
            new_prices[object]=current_prices[object]
    return new_prices,current_assignment
if __name__=='__main__':
    #价格矩阵
    value_matrix={
        ('A1', 'B1'): 4 , ('A1', 'B2'): 8 , ('A1', 'B3'): 17, ('A1', 'B4'): 10,
        ('A2', 'B1'): 14, ('A2', 'B2'): 18, ('A2', 'B3'): 17, ('A2', 'B4'): 7,
        ('A3', 'B1'): 9 , ('A3', 'B2'): 5 , ('A3', 'B3'): 14, ('A3', 'B4'): 10,
        ('A4', 'B1'): 17, ('A4', 'B2'): 18, ('A4', 'B3'): 14, ('A4', 'B4'): 6,
    }
    #竞拍者集合
    bidder_set=['A1','A2','A3','A4']
    #竞拍对象集合
    object_set = ['B1', 'B2', 'B3', 'B4']
    #每个竞拍者可竞拍对象集合
    available_objects_for_bidders={
        'A1': ['B1', 'B2', 'B3', 'B4'],
        'A2': ['B1', 'B2', 'B3', 'B4'],
        'A3': ['B1', 'B2', 'B3', 'B4'],
        'A4': ['B1', 'B2', 'B3', 'B4'],
    }
    #初始竞拍结果（满足ε互补松弛条件）
    current_assignment = {'A1': 'B3', 'A2': 'B2'}
    current_assignment = {}
    #初始报价
    current_prices = {'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0}
    #ε阈值
    epsilon=1.0
    #竞拍过程
    k=1
    while True:
        new_bid=bidding(current_assignment,current_prices)
        if len(new_bid)>0:
            new_price,new_assignment=assigning(new_bid,current_assignment,current_prices)
            current_assignment=new_assignment
            current_prices=new_price
        else:
            break
        k += 1
        print("第{}次竞拍：".format(k))
        print("\t竞拍结果为：")
        print("\t",current_assignment)
        print("\t最新定价为：")
        print("\t",current_prices)
    print("hello,world")