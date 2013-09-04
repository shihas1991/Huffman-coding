function frequency(str)
{
	var freqs={};
	var len=str.length;
	for (var i=0;i<len;i++)
	{
		var x=str[i];
		if (freqs[x]==undefined)
		{
			freqs[x]=1;
		}
		else
		{
			freqs[x]+=1;
		}
	}
	return freqs;
}
freqs=frequency('aaabbccccdeffffgg');
/*console.log(freqs);*/
function sortfreq(freqs)
{
	letters=[];
	for (var key in freqs)
		letters.push([freqs[key],key]);
	return (letters.sort());
}
tuples=sortfreq(freqs);
/*console.log(tuples);*/
function buildtree(tuples)
{
	while ((tuples.length)>1)
	{
		var leasttwo=tuples.slice(0,2);
		var therest=tuples.slice(2,tuples.length);
		var combfreq=leasttwo[0][0]+leasttwo[1][0];
		tuples=therest;
		var branch=[combfreq,leasttwo];
		tuples.push(branch);
		tuples.sort();
	}
	return tuples[0]
}
tree=buildtree(tuples);
/*console.log(tree);*/
function trimtree(tree)
{
	var p=tree[1];
	if (typeof p=='string')
	{
		return p;
	}
	else
	{
		return Array(trimtree(p[0]),trimtree(p[1]));
	}
}
/*console.log(trimtree(tree));*/
var codes={};
function assigncodes(node,pat)
{
	pat=pat || '';
	if (typeof node=='string')
	{
		codes[node]=pat;
	}
	else
	{
		assigncodes(node[0], pat+"0")
		assigncodes(node[1], pat+"1") 
	}
}
assigncodes(trimtree(tree));
/*console.log(codes);*/
function encode(str)
{
	output='';
	for (var i=0;i<str.length;i++)
	{
		output=output+codes[str[i]];
	}
	return output;
}
var str=encode('aaabbccccdeffffgg');
/*console.log(str);*/
function decode(tree,str)
{
	output='';
	k=tree;
	for (var i=0;i<str.length;i++)
	{
		if (str[i]=='0')
		{
			k=k[0];
		}
		else
		{
			k=k[1];
		}
		if (typeof k=='string')
		{
			output=output+k;
			k=tree;
		}
	}
	return output;
}
console.log(str,decode(trimtree(tree),str));
