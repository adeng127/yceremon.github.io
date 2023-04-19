/*
    功能列表
    1，全选功�??
        选中所有行，汇总价�??
    2，单选功�??
        选中或取消选中一�??
    3，数量加减按�??
        增减商品数量，计算小计价�??
    4，删除按�??
        移除当前行，重新计算总计价格
    5，删除被选中的商�??
*/

// 获取所有加减按�??(得到的是一个数�??)
var add = document.querySelectorAll(".Increase");
var reduce = document.querySelectorAll(".Reduce");
// 获取所有文本框
var inputs = document.querySelectorAll(".unum");
// 获取所有行
var rows = document.querySelectorAll(".row");
// 获取所有单选框 
var chooses = document.querySelectorAll(".choose");
// 获取所有全选按�??
var choose_alls = document.querySelectorAll(".choose_all");
// 获取所有删除按�??
var btn_dels = document.querySelectorAll(".btn-del");
// 删除选中的商�??
var del_check = document.querySelector(".del_check");

rows[n-1].style.display="table-row"

document.getElementById('size-display1').textContent = s+c;


// 给所有的加减按钮绑定点击事件
for(var i=0; i<add.length; i++){
    add[i].onclick=function(){

        // 获取对应的父节点
        var amount = this.parentNode;
        // 获取文本�??
        var input = amount.querySelector(".unum");
        // 获取文本框中的数�??
        var num = input.value;
        num++;
        // 修改文本框的�??
        input.value=num;

        // 计算小计
        // 获取当前�??
        var tr =  amount.parentNode.parentNode;
        // 获取商品单价
        var unit = tr.querySelector(".unit");
        var price = unit.innerHTML;
        // 重新计算小计价格
        smallTotal = num*price;
        // 保留两位小数
        smallTotal = smallTotal.toFixed(2);

        // 将计算好的小计价格设置给金额
        var u_price = tr.querySelector(".u-price");
        u_price.innerHTML = smallTotal;

        // 使当前行被选中
        var choose = tr.querySelector(".choose");
        // 把它当成逻辑变量，赋true false也可�?? 
        choose.checked = "true";

        // 计算总计
        setTotal();
    }
}

for(var i=0; i<reduce.length; i++){
    reduce[i].onclick=function(){

        // 获取对应的父节点
        var amount = this.parentNode;
        // 获取文本�??
        var input = amount.querySelector(".unum");
        // 获取文本框中的数�??
        var num = input.value;
        if(num > 1){
            num--;
        }
        // 修改文本框的�??
        input.value=num;

        // 计算小计
        // 获取当前�??
        var tr =  amount.parentNode.parentNode;
        // 获取商品单价
        var unit = tr.querySelector(".unit");
        var price = unit.innerHTML;
        // 重新计算小计价格
        smallTotal = num*price;
        // 保留两位小数
        smallTotal = smallTotal.toFixed(2);

        // 将计算好的小计价格设置给金额
        var u_price = tr.querySelector(".u-price");
        u_price.innerHTML = smallTotal;

        // 使当前行被选中
        var choose = tr.querySelector(".choose");
        // 把它当成逻辑变量，赋true false也可�?? 
        choose.checked = "true";

        setTotal();
    }
}

// 用户手动修改文本框中的商品数�??
for(var i=0; i<inputs.length; i++){
    // 给每个文本框绑定 失焦 事件 
    inputs[i].onblur = function(){
        // 防止出现负数
        if(this.value < 1){
            this.value = 1;
        }
        // 防止输入小数或其它字�??
        this.value = parseInt(this.value);

        // 计算小计
        // 获取当前�??
        var tr =  this.parentNode.parentNode.parentNode;
        // 获取商品单价
        var unit = tr.querySelector(".unit");
        var price = unit.innerHTML;
        // 重新计算小计价格
        smallTotal = this.value*price;
        // 保留两位小数
        smallTotal = smallTotal.toFixed(2);

        // 将计算好的小计价格设置给金额
        var u_price = tr.querySelector(".u-price");
        u_price.innerHTML = smallTotal;

        // 使当前行被选中
        var choose = tr.querySelector(".choose");
        // 逻辑变量
        choose.checked = "true";

        setTotal();
    }
}

// 计算总计价格 & 计算选中的商品总数 & 同时判断是否全�?
function setTotal(){
    var total = 0;  // 商品总价
    var allNum = 0; // 商品总数
    // 重新获取�??
    rows = document.querySelectorAll(".row");
    // 遍历所有行
    for(var i=0; i<rows.length; i++){
        // 查找被选中的行
        var checkbox = rows[i].querySelector(".choose");
        if(checkbox.checked){
            
            // 获取小计价格（得到的是字符串，不是数字，需要转化）
            var smallTotal = rows[i].querySelector(".u-price").innerHTML;
            // 获取商品数量
            var num = rows[i].querySelector(".unum").value;
            // 把小计价格转化为数字
            smallTotal = Number(smallTotal);
            total += smallTotal;
            // 计算商品总数
            num = Number(num);
            allNum += num;
        }
    }

    // 把总计放在它应在的位置 
    var totalPrice = document.querySelector(".t-price");
    totalPrice.innerHTML = total.toFixed(2);
    // 设置商品总数
    document.querySelector(".t-number").innerHTML = allNum;

    var isCheckAll = true;
    for(var i=0; i<rows.length; i++){
        var checkbox = rows[i].querySelector(".choose");
        if(!checkbox.checked){
            isCheckAll = false;
            break;
        }
    }
    if(rows.length<=0){
        isCheckAll = false;
    }
    // 将两个全选框设置为和全选变量相同的�??
    choose_alls[0].checked = isCheckAll;
    choose_alls[1].checked = isCheckAll;
}

// 单选框点击事件 
for(var i=0; i<chooses.length; i++){
    chooses[i].onclick = function(){
        // 求一下总计就行�??
        setTotal();
    }
}

// 全选框点击事件
for(var i=0; i<choose_alls.length; i++){
    choose_alls[i].onclick = function(){
        // 全�?/全不选所有单选框
        for(var i=0; i<rows.length; i++){
            var checkbox = rows[i].querySelector(".choose");
            checkbox.checked = this.checked;
        }
        // 与另外一个全选框联动
        choose_alls[0].checked = this.checked;
        choose_alls[1].checked = this.checked;
        // 计算总计
        setTotal();
    }
}

// 删除当前�??
for(var i=0; i<btn_dels.length; i++){
    btn_dels[i].onclick = function(){
        var tr = this.parentNode.parentNode;
        tr.parentNode.removeChild(tr);//移出
        setTotal();//重新计算
    }
}

// 删除选中�??
del_check.onclick = function(){
    rows = document.querySelectorAll(".row");
    for(var i=0; i<rows.length; i++){
        var checkbox = rows[i].querySelector(".choose");
        if(checkbox.checked){
            rows[i].parentNode.removeChild(rows[i]);
        }
    }
}

function onel()
{
    alert("请关注微信公众号***登录后付款")
}

