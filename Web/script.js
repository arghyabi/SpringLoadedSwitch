function renderCountValues(data)
{
    let valueElement = document.getElementById('countDisplay');
    valueElement.innerHTML = "Count: " + data['currentVal'] + " / " + data['maxVal'];
}


function updateCountValues() {
    $.ajax({
        url: "postRequest.php",
        method: "POST",
        data: {
            getCountValues: 1,
        },
        success: function(data) {
            renderCountValues(data);
        }
    });
}


function updateTotalCountValue() {
    let valueElement = document.getElementById('totalCount');
    totalCount = valueElement.value;
    if (totalCount == "")
        return;

    $.ajax({
        url: "postRequest.php",
        method: "POST",
        data: {
            updateTotalCount: 1,
            newTotalCount   : totalCount,
        },
        success: function(data) {
            if(data['status'])
            {
                alert(data['msg']);
                valueElement.value = "";
            }
            else
            {
                alert(data['msg']);
            }
        }
    });
}


function updateCurrentCountValue() {
    let valueElement = document.getElementById('currentCount');
    currentCount = valueElement.value;
    if (currentCount == "")
        return;

    $.ajax({
        url: "postRequest.php",
        method: "POST",
        data: {
            updateCurrentCount: 1,
            newCurrentCount   : currentCount,
        },
        success: function(data) {
            if(data['status'])
            {
                alert(data['msg']);
                valueElement.value = "";
            }
            else
            {
                alert(data['msg']);
            }
        }
    });
}


setInterval(updateCountValues, 1000);
