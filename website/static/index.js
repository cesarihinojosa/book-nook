function addBook(book){
    fetch("/add-book",
    {method: "POST", 
    body: JSON.stringify({ book: book }),
    }).then((_res) => {
        window.location.href = "/add";
    });
}