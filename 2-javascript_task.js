function generateRandomNumber() {
    const randNum = new Promise ((resolve, reject)=> {
      setTimeout(() => {
        resolve (Math.random() % 2 * 10) + 1)
      
      });
}
randNum.then(Response =>{
  console.log(Response)
})
  
 
  