function addBook(bookID){
    fetch("/add-book",
    {method: "POST", 
    body: JSON.stringify({ bookID: bookID }),
    }).then((_res) => {
        window.location.href = "/";
    });
}