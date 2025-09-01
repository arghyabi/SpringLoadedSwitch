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


function updateSwitchType() {
    let valueElement = document.getElementById('switchType');
    let switchType = valueElement.value;

    $.ajax({
        url: "postRequest.php",
        method: "POST",
        data: {
            updateSwitchType: 1,
            newSwitchType: switchType,
        },
        success: function(data) {
            if(data['status'])
            {
                $('#switchTypeStatus').text(switchType);
                alert(data['msg']);
            }
            else
            {
                alert(data['msg']);
            }
        }
    });
}


function toggleMotor() {
    $.ajax({
        url: "postRequest.php",
        method: "POST",
        data: {
            toggleMotor: 1,
        },
        success: function(data) {
            if(data['status'])
            {
                $('#motorToggle').text(data['buttonText']);
                updateMotorStatus(data['motorStatus']);
                alert(data['msg']);
            }
            else
            {
                alert(data['msg']);
            }
        }
    });
}


function updateMotorStatus(status) {
    let statusElement = $('#motorStatus');
    let buttonElement = $('#motorToggle');
    statusElement.text(status == 1 ? 'ON' : 'OFF');
    if (status == 1) {
        buttonElement.removeClass('motor-off').addClass('motor-on');
    } else {
        buttonElement.removeClass('motor-on').addClass('motor-off');
    }
}


setInterval(updateCountValues, 1000);
