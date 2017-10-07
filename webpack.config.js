const path = require("path");
const webpack = require("webpack");

ExtractTextPlugin = require("extract-text-webpack-plugin");



module.exports = {

  entry: {
    app: "./src/static/app.js",
  },

  output: {
    path: path.resolve(__dirname, "src/app/static"),
    filename: "[name].js"
  },

  devtool: "source-map",

  resolve: {
    alias: {
      templates: path.resolve(__dirname, "src/static/templates/")
    },
  },

  module: {

    rules:[{
      test: /.js$/,
      exclude: /(node_modules|bower)/,
      use: {
        loader: "babel-loader"
      }
    },{
      test: /\.css$/,
      use:  ExtractTextPlugin.extract({
        fallback: "style-loader",
        use: "css-loader"
      })
    },{
     test: /\.(woff|woff2|eot|ttf|otf|svg)$/,
     use: [
       'file-loader?name=[name].[ext]'
     ]
    },{
     test: /\.(png|svg|jpg|gif)$/,
     use: [
       'file-loader?name=[name].[ext]'
     ]
    }]
  },

  plugins: [
    new ExtractTextPlugin("vendor.css")
  ]
};