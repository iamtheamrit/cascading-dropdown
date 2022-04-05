const emptyOption = $("<option value=''>---------</option>");

function fetchOptions(id,data,childId=null){
    var url = $(id).attr("data-url");
    $.ajax({
      url: url,                 
      data: data,
      success: function (data) {
        $(id).html(data);
        if (childId){
            $(childId).html(emptyOption);
        }
      }
    });
}

if ($("#id_state").val()){
    fetchOptions("#id_district",{
        'state': $("#id_state").val()
      },"#id_village",)
}
$("#id_state").change(function () {
    fetchOptions("#id_district",{
        'state': $(this).val()
      },"#id_village",)
});

$("#id_district").change(function () {
    fetchOptions("#id_village",{
        'district': $(this).val()
      })
});
