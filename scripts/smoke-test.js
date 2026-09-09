const http=require('http');const port=process.env.PORT||10000;
const checks=['/api/health','/api/meta','/api/games','/api/modules','/'];let i=0;
function next(){if(i>=checks.length){console.log('SMOKE TEST PASSED');process.exit(0)}const p=checks[i++];http.get({host:'127.0.0.1',port,path:p},r=>{console.log(p,r.statusCode);r.resume();if(r.statusCode>=400)process.exit(1);r.on('end',next)}).on('error',e=>{console.error(e.message);process.exit(1)})}next();
