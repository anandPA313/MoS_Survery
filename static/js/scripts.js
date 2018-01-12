$(function()
  {
    $('#myform').validate(
      {
        rules:
        {
          Color:{ required:true }
        },
        messages:
        {
          Color:
          {
            required:"Please select a Value<br/>"
          }
        },
        errorPlacement: function(error, element)
        {
            if ( element.is(":radio") )
            {
                error.appendTo( element.parents('.container') );
            }
            else
            { // This is the default behavior
                error.insertAfter( element );
            }
         }
      });

  });
