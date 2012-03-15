$(document).ready(function()
                    {
                        $( "#datepicker" ).datepicker();
                        
                        $.getJSON('xhr_test',function(data){
                                                            $.each(data, function(entryIndex, entry) {
                                                                var pubDate = new Date(entry['fields']['datepicker']);
                                                                var eve = pubDate.getDate() + 1;
                                                                //var key = 'table.ui-datepicker-calendar tbody tr td a:contains(' + eve + ')';
                                                                
                                                                $('table.ui-datepicker-calendar tbody tr td a:contains(' + eve + ')').css({'color':'#EB8F00'}).attr({'href':'/events'});
                                                                $('table.ui-datepicker-calendar tbody tr td a:disabled');
                                                                $('table.ui-datepicker-calendar tbody tr td a').click(function()
                                                                        {
                                                                            
                                                                            return false;
                                                                        }
                                                );
                                                                });
                                                            
                                                            
                                                        }
                                );
                        //$('nav ul li a').click(function()
                        //                            {
                        //                                $.post('xhr_test', {name: "Monty",food: "Spam"},function(data)
                        //                                        {
                        //                                            alert(data);
                        //                                        }
                        //                                    );
                        //                                return false;
                        //                            }
                        //                        );
      
                    }
                );