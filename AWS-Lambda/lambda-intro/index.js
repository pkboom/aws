exports.handler = async (event, context, callback) => {
  console.log("Event: \n" + JSON.stringify(event, null, 2));
  console.log("Context: \n" + JSON.stringify(context, null, 2));

  return context.logStreamName;
};
