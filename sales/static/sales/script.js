
    let pages = 1;
    let loading = false;
    
    function loadMoreItems() {

        if (loading) return;
        loading = true;
    
        fetch(`/scroll?page=${pages}`)
            .then(response => response.json())
            .then(data => {
                data.data.forEach(item => {
                    const div = document.createElement('div');
                    div.classList.add('mb-3');
                    div.innerHTML = `
                        <button class="btn btn-primary w-100 p-3"
                            onclick="fix('${item.website_link}', '${item.name}')">
                            ${item.name} ${item.price} Units: Per ${item.unit}
                        </button>
                    `;
                    document.querySelector('#body').appendChild(div);
                });
    
                if (data.has_next) {
                    pages++;
                    loading = false;
                }
            });
    }
    
    // Trigger when scrolling near bottom

    // Initial load
    //loadMoreItems();
    document.querySelector('#allmenu').addEventListener('click', (e) => {
        e.preventDefault(); 
        page.innerHTML = ''; // Prevent any unintended behavior
        document.querySelector('#close').click();  // Close the menu
        loadMoreItems();
        window.addEventListener('scroll', () => {
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 300) {
                loadMoreItems();
            }
        });
        
    });

    document.querySelector('#contact').addEventListener('click',(e)=>{
        e.preventDefault();
        document.querySelector('#close').click();
        page.innerHTML = '<h1>Email: pimpy6565@gmail.com<br>Creator: Chris<br>Will get back to you as soon as i can!<br><b>Thank You!</b></h1><br>  <img src="static/sales/whale.png">'
    })