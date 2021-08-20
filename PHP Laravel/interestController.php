<?php

namespace App\Http\Controllers;

use App\Models\Category;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Session;
use Illuminate\View\View;

class InterestController extends Controller
{


    public function index()
    {
        $Categories_list = Category::all();
        $categories_users=User::find(auth()->user()->id);
        $category_order=$categories_users->categories;
        $category_orders=User::find(auth()->user()->id)->categories()->select('id','name','user_id','category_id')->get();

        $category_orders_category=Category::select('id','name')->get();
        $user=new User();// instance of the main model
        $user->findOrFail(auth()->user()->id)->categories->all();
        return view('profile.index', ['categories' => $Categories_list,
            'user_related'=>$user],compact('category_orders','category_orders_category'));
    }

    public function store(Request $request)
    {
        $inputs = request()->validate([
            'category_id' => 'nullable',

        ]);

        $user= new User();

        // OOP

        try {
        auth()->user()->categories()->attach($inputs);
        session::flash('success', 'تمت اضافة الاهتمام بنجاح');

        }catch (\Exception $e){
            session::flash('message', 'لا يمكنك اضافة هذا الاهتمام الى قائمتك لانه مضاف مسبقاً');
        }

        return back();
    }

    public function destroy($id)
    {


        try {
            auth()->user()->categories()->detach($id);

        }catch (\Exception $e){
            session::flash('message', 'تم ازالة اهتمام');
            return back();

        }

        return back();
    }


}
