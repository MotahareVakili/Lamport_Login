   function handleLogin() {
    const username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Prepare initial data for the AJAX request
    const initialData = {
        username: username,
        initlog:true
    };

    // Make the initial AJAX request
    fetch(BASE_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        body: JSON.stringify(initialData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.n);
        if(data.n==-1)
        {
          const errorMessage = 'You should change your password.';
          const userConfirmed = confirm(errorMessage);
           if (userConfirmed) {
        window.location.href = CHANGE_URL;
        } else {
        console.log('User clicked Cancel');
        }

        }

        else
        {

            for(let i=0;i<data.n;i++)
              password=CryptoJS.SHA256(password).toString();

            const updatedData = {
                username: username,
                password: password,
                initlog: false
            };

            // Make another AJAX request with the updated data
            fetch(BASE_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
                },
                body: JSON.stringify(updatedData)
            })
             .then(response => response.json())
                .then(responseData => {
                    console.log(responseData);

                    if (responseData.success) {

                        window.location.href = HOME_URL;
                    } else {

                        console.log('Login failed');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }



        })
    .catch(error => {
        console.error('Error:', error);
    });
}