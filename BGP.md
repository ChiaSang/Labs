
# BGP

--
The training of H3C SE
--

---
	端口号是179
	矢量路由协议
	基于TCP 的点到点的单播连接
	支持CIDR，只发送增量路由条目
	无环路（AS_PATH等防环机制）
	支持丰富的路由策略
	适用于大规模的网络环境 

### BGP的对等体
#### BGP的发言者与对等体
* 发送BGP 消息的路由器成为BGP 发言者（BGP Speaker）相互交换消息的BGP 发言者之间互称为BGP 对等体（BGP Peer）

#### 对等体之间的交互原则
* 从IBGP获得的路由不会发布给IBGP，只发布给EBGP对等体
* 从EBGP获得的路由会同时发布给IBGP对等体和EBGP对等体
* BGP只发送更新的路由和最优的路由

#### IBGP
* 从一个IBGP邻居收到的路由条目将不会传输给另一个IBGP(防环 )
* 从一个EBGP 邻居收到的路由条目将能够传输给自己的IBGP 和EBGP 邻居

#### EBGP
* 从一个EBGP 邻居收到的路由条目将传输给自己所有的邻居。

### BGP路由更新信息处理
BGP对等体发来的路由更新信息---Adj-RIB-In---应用路由策略---生成BGP路由表---最有的加入IP路由表---应用出策略---发送Adj-RIB-Out

#### BGP 路由通告原则
* 只有在同一AS 中，从一个IBGP 邻居收到的路由条目将不会传输给另一个IBGP，可以防环
* 可用的最有路由路由信息和可用的次优路由信息都会被通告，但是只有最优的会加入到IP路由表中

### BGP的报文
	1. OPEN报文:协商参数，建立邻居关系
	2. UPDATE报文:交换路由信息
	3. KEEPLIVE报文:保持邻居关系
	4. NOTIFICATION报文:通知消息，差错通知

### BGP的状态机
	1. Idle 空闲状态
	2. Connect 连接状态（准备建立TCP 连接）
	3. Active 激活状态（正在建立TCP 连接）
	4. Open-Sent（发送了Open 包）
	5. Open-Confirm（接受了Open 包，比较参数） 
	6. Established 已连接状态。只要有一个发生错误，立刻回到Idle
BGP 达到Established 状态，将会把自己本地所有的路由表通过Update 消息发送给邻居，以后就是增量更新了。

### BGP的数据库
* IP路由表:全局路由表包括了所有的路由信息
* BGP路由表:BGP数据库中的路由表包含从外部和本地学到的BGP路由信息
* Adj-RIB-In:对等体宣告给本地BGP Speaker的未处理的路由信息
* Adj-RIB-Out:本地BGP Speaker要宣告给其他对等体的路由信息

### BGP的同步
* 在IBGP路由加入路由表并发布给EBGP对等体之前，会先检查IGP路由表，只有IGP路由表中这条IBGP路由时才会加入并发布给EBGP

### BGP的属性
#### 公认必遵：所有路由必须识别的，存在于Update Message中
* Origin:路由信息的来源，IGP,EGP,INCOMLETED

> 路由的引入方式：network/import
>
> 在路由选择的时候，ORIGIN中，IGP优于EGP，EGP优于INCOMPLETE

* AS-Path:自治区域路径，按矢量顺序记录某条路由从本地到目的网段

> 作用：1. 防环 2.选路 
>
> AS Segment:
>
> Community 2种（AS Set）Common 2种（AS Secquence）

* Next-Hop:下一跳

>从EBGP收到的路由信息传递给其他IBGP时，下一跳属性不改变


#### 公认可选：所有路由可以识别，但是不是必须的
* Local-Pref:本地优先，表明路由器的优先级，判断离开AS时的最佳路由

#### 可选过渡：在BGP对等体之间传播

#### 可选非过渡：

* MED属性：用于判断进入AS时的最佳路由，影响的是入流量，越小越优先。


#### 团体属性：用于标示具有相同特征的路由

##### 自定义（私有）团体：AS内

##### 公有团体：

###### NO advise：收到有该属性的路由不通告

###### NO Expert：收到有该属性的路由不传递给EBGP邻居

###### NO Expert subconfed：不传递给联盟EBGP

##### 选路方式：

origin，as-path，local-pref，med，团体

##### 选路原则：

local-pref

本地生成

as-path短的

origin

med
